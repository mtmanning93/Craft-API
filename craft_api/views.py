from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE,
    JWT_AUTH_REFRESH_COOKIE,
    JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)
from profiles.models import Profile
from django.contrib.auth.models import User

@api_view(["DELETE"])
def delete_account(request, pk):
    # Check if the user making the request is the same as the one to be deleted
    if request.user.id != int(pk):
        return Response({"error": "You do not have permission to delete this user."}, status=status.HTTP_403_FORBIDDEN)

    try:
        # Get the user and profile with the specified pk
        user = User.objects.get(pk=pk)
        profile = Profile.objects.get(owner=user)

        # Delete the user and profile
        user.delete()
        profile.delete()

        # Logout the user by clearing cookies
        response = Response({"result": "User and profile deleted."}, status=status.HTTP_200_OK)
        response.set_cookie(
            key=JWT_AUTH_COOKIE,
            value="",
            httponly=True,
            expires="Thu, 01 Jan 1970 00:00:00 GMT",
            max_age=0,
            samesite=JWT_AUTH_SAMESITE,
            secure=JWT_AUTH_SECURE,
        )
        response.set_cookie(
            key=JWT_AUTH_REFRESH_COOKIE,
            value="",
            httponly=True,
            expires="Thu, 01 Jan 1970 00:00:00 GMT",
            max_age=0,
            samesite=JWT_AUTH_SAMESITE,
            secure=JWT_AUTH_SECURE,
        )
        return response

    except User.DoesNotExist:
        raise Http404("User not found.")
    except Profile.DoesNotExist:
        raise Http404("Profile not found.")

@api_view()
def root_route(request):
    return Response(
        {
            "message": (
                "Welcome to the craft-api, " "built for the Craft social media app."
            )
        }
    )


@api_view(["POST"])
def logout_route(request):
    # Fix for DRF logout bug from Code Institutes
    # DRF walkthrough
    print("Performing logout")
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value="",
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value="",
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
