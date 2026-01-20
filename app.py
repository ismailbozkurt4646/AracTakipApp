from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    import os
    # Render portu dinamik olarak atar, bulamazsa varsayılan 5000'i kullanır
    port = int(os.environ.get("PORT", 5000))
    # host="0.0.0.0" dış erişim için kritiktir
    app.run(host="0.0.0.0", port=port)