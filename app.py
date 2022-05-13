from flask import Flask, jsonify, request, json

app=Flask(__name__)

@app.route('/test', methods=['POST'])
def string_cutter():
    #retrieve and store string to be cut
    user_string=request.json
    string_to_cut=user_string['string_to_cut']
    #empty string object that will concatenate and store eligible letters
    return_string=''
    #loop through each letter; extract and concatenate every third letter
    for letter in range(len(string_to_cut)):
        if (letter+1)%3==0:
            return_string=return_string+string_to_cut[letter]
    return jsonify({'return_string':return_string})

if __name__=='__main__':
    app.run(debug=True)
