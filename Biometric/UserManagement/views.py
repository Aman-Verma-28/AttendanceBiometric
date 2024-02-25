from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserRegistraion, UserAttendance, Item
from rest_framework.response import Response
from rest_framework import status
import datetime

# Create your views here.


class EntryView(APIView):
    def get(self, request):
        try:
            data = request.data
            token = data.get("token")

            if not token:
                users = UserAttendance.objects.filter(is_active=True).values(
                    "user__name", "user__role", "entry", "item__name"
                )
                return Response({"users": users}, status=status.HTTP_200_OK)
            else:
                user = UserRegistraion.objects.get(token=token)
                user_attendance = UserAttendance.objects.filter(
                    user=user, is_active=True
                ).values("entry", "exit", "item__name")
                return Response(
                    {"user_attendance": user_attendance}, status=status.HTTP_200_OK
                )

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data
            token = data.get("token")
            item_token = data.get("item_token")
            user = UserRegistraion.objects.get(token=token)
            item = Item.objects.get(token=item_token)
            UserAttendance.objects.create(user=user, item=item, is_active=True)

            return Response({"message": "Entry Recorded"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ExitView(APIView):
    def post(self, request):
        try:
            data = request.data
            token = data.get("token")

            user = UserRegistraion.objects.get(token=token)
            user_attendance = UserAttendance.objects.get(user=user, is_active=True)
            user_attendance.exit = datetime.datetime.now()
            user_attendance.is_active = False
            user_attendance.save()

            return Response({"message": "Exit Recorded"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
