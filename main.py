from flask import Flask, render_template, jsonify, request
from control import RobotMove

app = Flask(__name__)
app.config.update(dict(TITLE='Raspberry PI mobile control'))


robot = RobotMove()
   
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/index/robotMove', methods=['GET', 'POST'])
def robotMove():
    move_val = request.get_json()
    forward_backward = int(move_val['x'])
    left_right = int(move_val['y'])
    
    def update():
        if forward_backward < 80:
            speed = 4 * (80 - forward_backward)
            if speed > 98: speed = 98
            robot.move(speed, dirL=True, dirR=False)
        elif forward_backward > 100:
            speed = 4 * (forward_backward - 100)
            if speed > 98: speed = 98
            robot.move(speed, dirL=False, dirR=True)
        elif left_right < 80:
            speed = 4 * (80 - left_right)
            if speed > 98: speed = 98
            robot.move(speed, dirL=False, dirR=False)
        elif left_right > 100:
            speed = 4 * (left_right)
            if speed > 98: speed = 98
            robot.move(speed, dirL=True, dirR=True)
        else:
            robot.move(speed=0, dirL=False, dirR=True)
            
        
    update()
    
    return 'move'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)







