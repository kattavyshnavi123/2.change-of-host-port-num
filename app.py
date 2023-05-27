from flask import Flask

FAI=Flask(__name__)
# flask function 1
#flask application instance
@FAI.route('/ff1/<na>/')
def ff1(na):
    return 'This is first flask file'
if __name__=='__main__':
    FAI.run(debug=True,host=''port=5001)    

