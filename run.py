from app import create_app

app = create_app()

if __name__ == "__main__":
    # Defina a porta desejada, por exemplo, 9090
    app.run(debug=True, port=9090)
