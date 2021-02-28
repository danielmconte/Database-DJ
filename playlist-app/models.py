"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE name description
    __tablename__ = 'playlists'

    def __repr__(self):
        p = self
        return f"<Playlist id={p.id} name={p.name} description={p.description}>"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    name = db.Column(db.String(20),
                    nullable=False,
                    unique=True)

    description = db.Column(db.String(200))



class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE title artist
    __tablename__ = 'songs'

    def __repr__(self):
        s = self
        return f"<Song id={s.id} title={s.title} artist={s.artist}>"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    title = db.Column(db.String(50),
                    nullable=False,
                    unique=True)

    artist = db.Column(db.String(30),
                    nullable=False,
                    unique=True)


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE playlist_id song_id
    __tablename__ = 'playlistsongs'

    def __repr__(self):
        p = self
        return f"<PlaylistSong id={p.id} playlist_id={p.playlist_id} song_id={p.song_id}>"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'))
    
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))

    
    song = db.relationship('Song', backref = 'playlists')

    playlist = db.relationship('Playlist', backref = 'songs')

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
