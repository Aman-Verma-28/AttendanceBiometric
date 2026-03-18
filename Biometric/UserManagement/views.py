from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item, UserAttendance, UserRegistraion


class EntryView(APIView):
    def get(self, request):
        try:
            token = request.query_params.get("token")

            if not token:
                users = UserAttendance.objects.filter(is_active=True).values(
                    "user__name", "user__role", "entry", "item__name"
                )
                return Response({"users": list(users)}, status=status.HTTP_200_OK)
            else:
                user = UserRegistraion.objects.get(token=token)
                user_attendance = UserAttendance.objects.filter(
                    user=user, is_active=True
                ).values("entry", "exit", "item__name")
                return Response(
                    {"user_attendance": list(user_attendance)},
                    status=status.HTTP_200_OK,
                )

        except UserRegistraion.DoesNotExist:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"message": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        try:
            data = request.data
            token = data.get("token")
            item_token = data.get("item_token")
            user = UserRegistraion.objects.get(token=token)
            item = Item.objects.get(token=item_token)
            UserAttendance.objects.create(user=user, item=item, is_active=True)

            return Response(
                {"message": "Entry Recorded"}, status=status.HTTP_201_CREATED
            )
        except (UserRegistraion.DoesNotExist, Item.DoesNotExist):
            return Response(
                {"message": "User or Item not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"message": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )


class ExitView(APIView):
    def post(self, request):
        try:
            data = request.data
            token = data.get("token")

            user = UserRegistraion.objects.get(token=token)
            user_attendance = UserAttendance.objects.get(user=user, is_active=True)
            user_attendance.exit = timezone.now()
            user_attendance.is_active = False
            user_attendance.save()

            return Response(
                {"message": "Exit Recorded"}, status=status.HTTP_200_OK
            )
        except UserRegistraion.DoesNotExist:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except UserAttendance.DoesNotExist:
            return Response(
                {"message": "No active attendance record found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"message": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )
