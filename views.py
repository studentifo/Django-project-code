from rest_framework import generics, permissions
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]

class WorkList(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically add the current user as the artist when creating a new work
        serializer.save(artists=[self.request.user.artist])

class WorkFilteredList(generics.ListAPIView):
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        work_type = self.kwargs['work_type']
        return Work.objects.filter(work_type=work_type)

class ArtistSearchList(generics.ListAPIView):
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        artist_name = self.kwargs['artist_name']
        return Artist.objects.filter(name__icontains=artist_name)
