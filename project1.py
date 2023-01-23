from flask import Flask, render_template, request
# Since we are using form and get input from the user, we need to get request. and we are using html, we need to get render_template.

# I need to create a flask object. 
app = Flask(__name__)
# We need to write a function that converts decimal number into roman number. So, first I'll write a function and I'll put it into  web application.
def convert(decimal_num):
    #I'll write a function named 'convert' and I'll pass an argument decimal_number. I'll convert this number into roman numeral. For sake of this project, you should be familiar with the coding a little bit. Your python knowledge is enough to solve this problem I thing. I'll use dictionary which has numbers as keys and their roman numbers as values. (the Roman numeral equivalent of this number)
    roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    # I create an empty string and it will hold my roman number
    num_to_roman = ''
    # I'll use for loop to create result. I'll divide the decimal number by dictionary keys from top to the end. I need to find out how many for example 1000 does decimal_num has. And then I'll multiply this number with value of key. 
    for i in roman.keys():
        num_to_roman += roman[i]*(decimal_num//i) # (decimal_num//i) gives us quotient of division
        # I need to get remainder of division of decimal_num by i
        decimal_num %= i
    return num_to_roman
    # Try a couple of examples. Of course, you all might have different functions

# Lets start to write our decorators. I'll use this function to pass result of user input. !!!Show index html file and explain the web page.!!! We need to sent not_valid and developer_name variable from here. I'll bind post and get part with '/' root path. And then, when the user gives us input, this input should be sent into application with POST method. If the user comes directly our web-page, at this time our method will be GET right. 
@app.route('/', methods=['POST', 'GET'])
def main_post():
    if request.method == 'POST':
        alpha = request.form['number']
        # I need to check two conditions. First If the number is decimal or not, second, If the number  less than 1 and greater than 3999. If the number has one of them, warning massage must raise. 
        # Regarding decimal control, If it has got at least one character which isn't decimal, warning  massage will raise. I am going to check it with isdecimal method. This method will return True,  if characters of alpha are decimal. On the other hand, If the number has at least one character  which is not decimal, it will return False. 
        if not alpha.isdecimal():
            return render_template('index.html', developer_name='Serdar', not_valid=True)
        # Secondly, I need to check If the number is between 1 to 3999 or not. To do this, I need to    convert my number to integer. Don't forget, when I call the number from html file and assign it    to the variable within application, this variable is going to be string. Thats why I need to   convert it into integer. 
        number = int(alpha)
        if not 0 < number < 4000:
            return render_template('index.html', developer_name='Serdar', not_valid=True)
        return render_template('result.html', number_decimal = number , number_roman= convert(number), developer_name='Serdar')
    else:
        # When user requests my web page, index.html will have to appear without "if condition". if the user gives us unexpected variable, This if condition will appear. This is the GET method. There is no any SENT activity. Just get the web page. I will put my name as developer_name and 
        return render_template('index.html', developer_name='Serdar', not_valid=False)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)

#All the setup is done, We have application and we have templates. Lets start statement. Lets go ahead and check if it is running. 
