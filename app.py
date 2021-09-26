from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """ 
        Display calculator 
    """
    return render_template('calculator.html')

@app.route('/operation_result/', methods=['POST'])
def operation_result():
    """
        Route to send calculator input
    """

    input1 = request.form['Input1']  
    input2 = request.form['Input2']
    input3 = request.form['Input3']
    input4 = request.form['Input4']
    input5 = request.form['Input5']
    input6 = request.form['Input6']
    
    try:
        token_price_a_initial = float(input1)
        token_price_b_initial = float(input2)
        token_price_a_future = float(input3)
        token_price_b_future = float(input4)
        token_a_pool_weight = float(input5)
        token_b_pool_weight = float(input6)
        if token_a_pool_weight + token_b_pool_weight == 1:

            r1 = token_price_a_future/token_price_a_initial 
            r2 = token_price_b_future/token_price_b_initial

            impermanent_loss = ((r1**(token_a_pool_weight))*(r2**(token_b_pool_weight))
                /(r1*token_a_pool_weight + r2*token_b_pool_weight) - 1)*-100

            return render_template(
                'calculator.html',
                result=impermanent_loss,
                calculation_success=True
            )

    except:
        return render_template(
            'calculator.html',
            calculation_success=False
        )
        
if __name__ == '__main__':
    app.debug = True
    app.run()