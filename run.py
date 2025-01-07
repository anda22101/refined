from flaskapp import app, db, socketio

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    # Use socketio.run only in development; for production, use Gunicorn instead
    socketio.run(app, host="0.0.0.0", port=5000, debug=False)
