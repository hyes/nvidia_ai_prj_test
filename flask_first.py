# 터미널에서 pip install flask 먼저 다운. settings에서 받는거 너무 느림...이유는 모르겠음.

# 폴더 구성
# pythonProject
# --flask_first : api서버역할
# --templates(frontend)
# ----first_template.html

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        #사용자가 어떤 정보를 입력하고 그 정보를 보낸 상황이라면,
        number1 = request.form.get('number1', type=float)
        number2 = request.form.get('number2', type=float)
        operation = request.form.get('operation')
        # print(number1, number2)

        if operation == 'add':
            result = number1 + number2
            print(result)
        elif operation == 'subtract':
            result = number1 - number2
            print(result)
        elif operation == 'divide':
            if number2 == 0:
                result = "오류: 0입력"
            else:
                result = number1/number2
        elif operation == 'multiply':
            result = number1 * number2
        return render_template('first_template.html', result = result)
    else:
        return render_template('first_template.html', result = None)


if __name__ == '__main__':
    app.run(debug=True)