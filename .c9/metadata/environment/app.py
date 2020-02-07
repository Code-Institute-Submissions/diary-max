{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":74,"column":21},"end":{"row":74,"column":22},"action":"insert","lines":["s"],"id":790},{"start":{"row":74,"column":22},"end":{"row":74,"column":23},"action":"insert","lines":["k"]}],[{"start":{"row":74,"column":23},"end":{"row":74,"column":24},"action":"insert","lines":["s"],"id":791}],[{"start":{"row":82,"column":8},"end":{"row":82,"column":10},"action":"remove","lines":["s3"],"id":792},{"start":{"row":82,"column":8},"end":{"row":82,"column":9},"action":"insert","lines":["t"]},{"start":{"row":82,"column":9},"end":{"row":82,"column":10},"action":"insert","lines":["a"]},{"start":{"row":82,"column":10},"end":{"row":82,"column":11},"action":"insert","lines":["s"]},{"start":{"row":82,"column":11},"end":{"row":82,"column":12},"action":"insert","lines":["k"]},{"start":{"row":82,"column":12},"end":{"row":82,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":96,"column":52},"end":{"row":97,"column":0},"action":"insert","lines":["",""],"id":793},{"start":{"row":97,"column":0},"end":{"row":97,"column":4},"action":"insert","lines":["    "]},{"start":{"row":97,"column":4},"end":{"row":98,"column":0},"action":"insert","lines":["",""]},{"start":{"row":98,"column":0},"end":{"row":98,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":98,"column":4},"end":{"row":104,"column":0},"action":"insert","lines":["#############################RECIPE SEARCH##########################################","@app.route('/recipe_search', methods = ['POST'])","def recipe_search():      ","    recipes_list = Recipe.query.filter(Recipe.recipe_name.ilike(\"%\" + request.form['recipe_name'] + \"%\")).all()","    recipe_count = Recipe.query.filter(Recipe.recipe_name.ilike(\"%\" + request.form['recipe_name'] + \"%\")).count()","    return render_template('index.html', recipe_count=str(recipe_count), recipes_list=recipes_list)",""],"id":794}],[{"start":{"row":103,"column":29},"end":{"row":103,"column":33},"action":"remove","lines":["ndex"],"id":795},{"start":{"row":103,"column":28},"end":{"row":103,"column":29},"action":"remove","lines":["i"]}],[{"start":{"row":103,"column":28},"end":{"row":103,"column":29},"action":"insert","lines":["t"],"id":796},{"start":{"row":103,"column":29},"end":{"row":103,"column":30},"action":"insert","lines":["a"]},{"start":{"row":103,"column":30},"end":{"row":103,"column":31},"action":"insert","lines":["s"]},{"start":{"row":103,"column":31},"end":{"row":103,"column":32},"action":"insert","lines":["k"]}],[{"start":{"row":103,"column":32},"end":{"row":103,"column":33},"action":"insert","lines":["s"],"id":797}],[{"start":{"row":73,"column":0},"end":{"row":104,"column":0},"action":"remove","lines":["#################AWS_S3_file_upload###########################","def upload_file_to_tasks(file, bucket_name, acl=\"public-read\"):","","    \"\"\"","    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html","    \"\"\"","","    try:","","        tasks.upload_fileobj(","            file,","            bucket_name,","            file.filename,","            ExtraArgs={","                \"ACL\": acl,","                \"ContentType\": file.content_type","            }","        )","","    except Exception as e:","        print(\"Something Happened: \", e)","        return e","","    return \"{}{}\".format(S3_LOCATION, file.filename)","    ","    #############################RECIPE SEARCH##########################################","@app.route('/recipe_search', methods = ['POST'])","def recipe_search():      ","    recipes_list = Recipe.query.filter(Recipe.recipe_name.ilike(\"%\" + request.form['recipe_name'] + \"%\")).all()","    recipe_count = Recipe.query.filter(Recipe.recipe_name.ilike(\"%\" + request.form['recipe_name'] + \"%\")).count()","    return render_template('tasks.html', recipe_count=str(recipe_count), recipes_list=recipes_list)",""],"id":798}],[{"start":{"row":63,"column":9},"end":{"row":63,"column":19},"action":"remove","lines":["vegetarian"],"id":799}],[{"start":{"row":63,"column":9},"end":{"row":63,"column":19},"action":"insert","lines":["vegetarian"],"id":800}],[{"start":{"row":67,"column":0},"end":{"row":68,"column":0},"action":"insert","lines":["",""],"id":801},{"start":{"row":68,"column":0},"end":{"row":69,"column":0},"action":"insert","lines":["",""]},{"start":{"row":69,"column":0},"end":{"row":70,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":68,"column":0},"end":{"row":68,"column":1},"action":"insert","lines":["@"],"id":802},{"start":{"row":68,"column":1},"end":{"row":68,"column":2},"action":"insert","lines":["a"]},{"start":{"row":68,"column":2},"end":{"row":68,"column":3},"action":"insert","lines":["a"]}],[{"start":{"row":68,"column":2},"end":{"row":68,"column":3},"action":"remove","lines":["a"],"id":803}],[{"start":{"row":68,"column":2},"end":{"row":68,"column":3},"action":"insert","lines":["p"],"id":804},{"start":{"row":68,"column":3},"end":{"row":68,"column":4},"action":"insert","lines":["p"]},{"start":{"row":68,"column":4},"end":{"row":68,"column":5},"action":"insert","lines":["."]}],[{"start":{"row":68,"column":5},"end":{"row":68,"column":6},"action":"insert","lines":["r"],"id":805},{"start":{"row":68,"column":6},"end":{"row":68,"column":7},"action":"insert","lines":["o"]},{"start":{"row":68,"column":7},"end":{"row":68,"column":8},"action":"insert","lines":["u"]}],[{"start":{"row":68,"column":5},"end":{"row":68,"column":8},"action":"remove","lines":["rou"],"id":806},{"start":{"row":68,"column":5},"end":{"row":68,"column":10},"action":"insert","lines":["route"]}],[{"start":{"row":68,"column":10},"end":{"row":68,"column":12},"action":"insert","lines":["()"],"id":807}],[{"start":{"row":68,"column":11},"end":{"row":68,"column":13},"action":"insert","lines":["''"],"id":808}],[{"start":{"row":68,"column":12},"end":{"row":68,"column":13},"action":"insert","lines":["e"],"id":809},{"start":{"row":68,"column":13},"end":{"row":68,"column":14},"action":"insert","lines":["d"]},{"start":{"row":68,"column":14},"end":{"row":68,"column":15},"action":"insert","lines":["i"]},{"start":{"row":68,"column":15},"end":{"row":68,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":68,"column":16},"end":{"row":68,"column":17},"action":"insert","lines":["_"],"id":810}],[{"start":{"row":68,"column":17},"end":{"row":68,"column":18},"action":"insert","lines":["t"],"id":811},{"start":{"row":68,"column":18},"end":{"row":68,"column":19},"action":"insert","lines":["a"]},{"start":{"row":68,"column":19},"end":{"row":68,"column":20},"action":"insert","lines":["s"]},{"start":{"row":68,"column":20},"end":{"row":68,"column":21},"action":"insert","lines":["k"]}],[{"start":{"row":68,"column":21},"end":{"row":68,"column":22},"action":"insert","lines":["/"],"id":812}],[{"start":{"row":68,"column":22},"end":{"row":68,"column":23},"action":"insert","lines":["<"],"id":813},{"start":{"row":68,"column":23},"end":{"row":68,"column":24},"action":"insert","lines":["t"]},{"start":{"row":68,"column":24},"end":{"row":68,"column":25},"action":"insert","lines":["a"]}],[{"start":{"row":68,"column":25},"end":{"row":68,"column":26},"action":"insert","lines":["s"],"id":814},{"start":{"row":68,"column":26},"end":{"row":68,"column":27},"action":"insert","lines":["k"]}],[{"start":{"row":68,"column":27},"end":{"row":68,"column":28},"action":"insert","lines":["_"],"id":815},{"start":{"row":68,"column":28},"end":{"row":68,"column":29},"action":"insert","lines":["i"]},{"start":{"row":68,"column":29},"end":{"row":68,"column":30},"action":"insert","lines":["d"]}],[{"start":{"row":68,"column":30},"end":{"row":68,"column":31},"action":"insert","lines":[">"],"id":816}],[{"start":{"row":68,"column":12},"end":{"row":68,"column":13},"action":"insert","lines":["/"],"id":817}],[{"start":{"row":68,"column":34},"end":{"row":69,"column":0},"action":"insert","lines":["",""],"id":818},{"start":{"row":69,"column":0},"end":{"row":69,"column":1},"action":"insert","lines":["d"]},{"start":{"row":69,"column":1},"end":{"row":69,"column":2},"action":"insert","lines":["e"]},{"start":{"row":69,"column":2},"end":{"row":69,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":69,"column":3},"end":{"row":69,"column":4},"action":"insert","lines":[" "],"id":819},{"start":{"row":69,"column":4},"end":{"row":69,"column":5},"action":"insert","lines":["e"]},{"start":{"row":69,"column":5},"end":{"row":69,"column":6},"action":"insert","lines":["d"]},{"start":{"row":69,"column":6},"end":{"row":69,"column":7},"action":"insert","lines":["i"]},{"start":{"row":69,"column":7},"end":{"row":69,"column":8},"action":"insert","lines":["t"]}],[{"start":{"row":69,"column":8},"end":{"row":69,"column":9},"action":"insert","lines":["_"],"id":820},{"start":{"row":69,"column":9},"end":{"row":69,"column":10},"action":"insert","lines":["t"]},{"start":{"row":69,"column":10},"end":{"row":69,"column":11},"action":"insert","lines":["a"]},{"start":{"row":69,"column":11},"end":{"row":69,"column":12},"action":"insert","lines":["s"]},{"start":{"row":69,"column":12},"end":{"row":69,"column":13},"action":"insert","lines":["k"]}],[{"start":{"row":69,"column":13},"end":{"row":69,"column":15},"action":"insert","lines":["()"],"id":821}],[{"start":{"row":69,"column":14},"end":{"row":69,"column":15},"action":"insert","lines":["t"],"id":822},{"start":{"row":69,"column":15},"end":{"row":69,"column":16},"action":"insert","lines":["a"]},{"start":{"row":69,"column":16},"end":{"row":69,"column":17},"action":"insert","lines":["s"]},{"start":{"row":69,"column":17},"end":{"row":69,"column":18},"action":"insert","lines":["k"]},{"start":{"row":69,"column":18},"end":{"row":69,"column":19},"action":"insert","lines":["_"]}],[{"start":{"row":69,"column":19},"end":{"row":69,"column":20},"action":"insert","lines":["i"],"id":823},{"start":{"row":69,"column":20},"end":{"row":69,"column":21},"action":"insert","lines":["d"]}],[{"start":{"row":69,"column":22},"end":{"row":69,"column":23},"action":"insert","lines":[":"],"id":824}],[{"start":{"row":69,"column":23},"end":{"row":70,"column":0},"action":"insert","lines":["",""],"id":825},{"start":{"row":70,"column":0},"end":{"row":70,"column":4},"action":"insert","lines":["    "]},{"start":{"row":70,"column":4},"end":{"row":70,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":70,"column":5},"end":{"row":70,"column":6},"action":"insert","lines":["h"],"id":826},{"start":{"row":70,"column":6},"end":{"row":70,"column":7},"action":"insert","lines":["e"]},{"start":{"row":70,"column":7},"end":{"row":70,"column":8},"action":"insert","lines":["_"]},{"start":{"row":70,"column":8},"end":{"row":70,"column":9},"action":"insert","lines":["t"]},{"start":{"row":70,"column":9},"end":{"row":70,"column":10},"action":"insert","lines":["a"]},{"start":{"row":70,"column":10},"end":{"row":70,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":70,"column":11},"end":{"row":70,"column":12},"action":"insert","lines":["k"],"id":827}],[{"start":{"row":70,"column":12},"end":{"row":70,"column":13},"action":"insert","lines":[" "],"id":828},{"start":{"row":70,"column":13},"end":{"row":70,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":70,"column":14},"end":{"row":70,"column":15},"action":"insert","lines":[" "],"id":829},{"start":{"row":70,"column":15},"end":{"row":70,"column":16},"action":"insert","lines":["m"]},{"start":{"row":70,"column":16},"end":{"row":70,"column":17},"action":"insert","lines":["o"]},{"start":{"row":70,"column":17},"end":{"row":70,"column":18},"action":"insert","lines":["n"]},{"start":{"row":70,"column":18},"end":{"row":70,"column":19},"action":"insert","lines":["g"]},{"start":{"row":70,"column":19},"end":{"row":70,"column":20},"action":"insert","lines":["o"]}],[{"start":{"row":70,"column":20},"end":{"row":70,"column":21},"action":"insert","lines":[","],"id":830},{"start":{"row":70,"column":21},"end":{"row":70,"column":22},"action":"insert","lines":["d"]},{"start":{"row":70,"column":22},"end":{"row":70,"column":23},"action":"insert","lines":["b"]}],[{"start":{"row":70,"column":23},"end":{"row":70,"column":24},"action":"insert","lines":["."],"id":831},{"start":{"row":70,"column":24},"end":{"row":70,"column":25},"action":"insert","lines":["t"]},{"start":{"row":70,"column":25},"end":{"row":70,"column":26},"action":"insert","lines":["a"]},{"start":{"row":70,"column":26},"end":{"row":70,"column":27},"action":"insert","lines":["s"]}],[{"start":{"row":70,"column":27},"end":{"row":70,"column":28},"action":"insert","lines":["k"],"id":832},{"start":{"row":70,"column":28},"end":{"row":70,"column":29},"action":"insert","lines":["s"]}],[{"start":{"row":70,"column":29},"end":{"row":70,"column":30},"action":"insert","lines":["."],"id":833},{"start":{"row":70,"column":30},"end":{"row":70,"column":31},"action":"insert","lines":["f"]},{"start":{"row":70,"column":31},"end":{"row":70,"column":32},"action":"insert","lines":["i"]},{"start":{"row":70,"column":32},"end":{"row":70,"column":33},"action":"insert","lines":["n"]}],[{"start":{"row":70,"column":33},"end":{"row":70,"column":34},"action":"insert","lines":["d"],"id":834},{"start":{"row":70,"column":34},"end":{"row":70,"column":35},"action":"insert","lines":["_"]},{"start":{"row":70,"column":35},"end":{"row":70,"column":36},"action":"insert","lines":["o"]}],[{"start":{"row":70,"column":36},"end":{"row":70,"column":37},"action":"insert","lines":["n"],"id":835},{"start":{"row":70,"column":37},"end":{"row":70,"column":38},"action":"insert","lines":["e"]}],[{"start":{"row":70,"column":38},"end":{"row":70,"column":40},"action":"insert","lines":["()"],"id":836}],[{"start":{"row":70,"column":39},"end":{"row":70,"column":41},"action":"insert","lines":["{}"],"id":837}],[{"start":{"row":70,"column":40},"end":{"row":70,"column":42},"action":"insert","lines":["\"\""],"id":838}],[{"start":{"row":70,"column":41},"end":{"row":70,"column":42},"action":"insert","lines":["_"],"id":839}],[{"start":{"row":70,"column":42},"end":{"row":70,"column":43},"action":"insert","lines":["i"],"id":840},{"start":{"row":70,"column":43},"end":{"row":70,"column":44},"action":"insert","lines":["d"]}],[{"start":{"row":70,"column":45},"end":{"row":70,"column":46},"action":"insert","lines":[":"],"id":841}],[{"start":{"row":70,"column":46},"end":{"row":70,"column":54},"action":"insert","lines":["ObjectId"],"id":842}],[{"start":{"row":70,"column":54},"end":{"row":70,"column":56},"action":"insert","lines":["()"],"id":843}],[{"start":{"row":70,"column":55},"end":{"row":70,"column":56},"action":"insert","lines":["t"],"id":844},{"start":{"row":70,"column":56},"end":{"row":70,"column":57},"action":"insert","lines":["a"]},{"start":{"row":70,"column":57},"end":{"row":70,"column":58},"action":"insert","lines":["s"]},{"start":{"row":70,"column":58},"end":{"row":70,"column":59},"action":"insert","lines":["k"]}],[{"start":{"row":70,"column":55},"end":{"row":70,"column":59},"action":"remove","lines":["task"],"id":845},{"start":{"row":70,"column":55},"end":{"row":70,"column":62},"action":"insert","lines":["task_id"]}],[{"start":{"row":70,"column":20},"end":{"row":70,"column":21},"action":"remove","lines":[","],"id":846}],[{"start":{"row":70,"column":20},"end":{"row":70,"column":21},"action":"insert","lines":["."],"id":847}],[{"start":{"row":68,"column":4},"end":{"row":70,"column":65},"action":"remove","lines":[".route('/edit_task/<task_id>')","def edit_task(task_id):","    the_task = mongo.db.tasks.find_one({\"_id\":ObjectId(task_id)})"],"id":848},{"start":{"row":68,"column":3},"end":{"row":68,"column":4},"action":"remove","lines":["p"]},{"start":{"row":68,"column":2},"end":{"row":68,"column":3},"action":"remove","lines":["p"]},{"start":{"row":68,"column":1},"end":{"row":68,"column":2},"action":"remove","lines":["a"]},{"start":{"row":68,"column":0},"end":{"row":68,"column":1},"action":"remove","lines":["@"]}],[{"start":{"row":47,"column":48},"end":{"row":47,"column":49},"action":"insert","lines":["s"],"id":849}],[{"start":{"row":47,"column":48},"end":{"row":47,"column":49},"action":"remove","lines":["s"],"id":850}],[{"start":{"row":47,"column":57},"end":{"row":47,"column":58},"action":"insert","lines":["s"],"id":851}],[{"start":{"row":47,"column":57},"end":{"row":47,"column":58},"action":"remove","lines":["s"],"id":852}],[{"start":{"row":45,"column":15},"end":{"row":45,"column":16},"action":"remove","lines":[" "],"id":853}],[{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"insert","lines":["s"],"id":854}],[{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"remove","lines":["s"],"id":855}],[{"start":{"row":43,"column":22},"end":{"row":43,"column":23},"action":"insert","lines":["s"],"id":856}],[{"start":{"row":43,"column":22},"end":{"row":43,"column":23},"action":"remove","lines":["s"],"id":857}],[{"start":{"row":26,"column":17},"end":{"row":26,"column":18},"action":"insert","lines":["s"],"id":858}],[{"start":{"row":26,"column":17},"end":{"row":26,"column":18},"action":"remove","lines":["s"],"id":859}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["t"],"id":860},{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":["a"]},{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["s"]},{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"insert","lines":["k"]}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["_"],"id":861}],[{"start":{"row":26,"column":13},"end":{"row":26,"column":18},"action":"remove","lines":["task_"],"id":862}],[{"start":{"row":26,"column":19},"end":{"row":26,"column":20},"action":"insert","lines":["s"],"id":863}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":9},"action":"remove","lines":["task_"],"id":864}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["t"],"id":865},{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":["a"]},{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["s"]},{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"insert","lines":["k"]},{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["-"]}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"remove","lines":["-"],"id":866}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["_"],"id":867}],[{"start":{"row":26,"column":13},"end":{"row":26,"column":14},"action":"insert","lines":["t"],"id":868},{"start":{"row":26,"column":14},"end":{"row":26,"column":15},"action":"insert","lines":["a"]},{"start":{"row":26,"column":15},"end":{"row":26,"column":16},"action":"insert","lines":["s"]},{"start":{"row":26,"column":16},"end":{"row":26,"column":17},"action":"insert","lines":["k"]},{"start":{"row":26,"column":17},"end":{"row":26,"column":18},"action":"insert","lines":["_"]}],[{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"remove","lines":["s"],"id":869}],[{"start":{"row":26,"column":24},"end":{"row":26,"column":25},"action":"remove","lines":["s"],"id":870}],[{"start":{"row":26,"column":24},"end":{"row":26,"column":25},"action":"insert","lines":["s"],"id":871}],[{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"insert","lines":["s"],"id":872}],[{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"remove","lines":["s"],"id":873}],[{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"insert","lines":["s"],"id":874}],[{"start":{"row":0,"column":0},"end":{"row":76,"column":0},"action":"remove","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"]= 'mongodb+srv://ayaanh221:missayaan221@myfirstcluster-lj4yz.mongodb.net/diary-max?retryWrites=true&w=majority'","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","@app.route('/add_task')","def add_task():","    ","    return render_template('addtask.html',","                           categories=mongo.db.categories.find())","","                           ","@app.route('/task_recipes')","def task_recipes():","    return render_template(\"recipes.html\", tasks=mongo.db.tasks.find())","    ","","@app.route('/insert_task', methods=['POST'])","def insert_task():","   ","    tasks = mongo.db.tasks","    tasks.insert_one(request.form.to_dict())","    return redirect(url_for('get_tasks'))","    ","    ","    ","","","","@app.route('/edit_task/<task_id>')","def edit_task(task_id):","    the_task = mongo.db.tasks.find_one({\"_id\": ObjectId(task_id)})","    all_categories =  mongo.db.categories.find()","    return render_template('edittask.html', task=the_task,","                           categories=all_categories)","","   ","   ","@app.route('/update_task/<get_tasks>', methods=[\"POST\"])","def update_task(task_id):","    tasks = mongo.db.tasks","    tasks.update( {'_id': ObjectId(task_id)},","    {","       'recipe_name':request.form.get('recipe_name'),","        'photo_link':request.form.get('photo_link'),","        'cooking_time': request.form.get('cooking_time'),","        'ingredients': request.form.get('ingredients'),","        'method': request.form.get('method'),","        'due_date': request.form.get('due_date'),","        'vegetarian':request.form.get('vegetarian')","    })","    return redirect(url_for('get_tasks'))","","","","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)","            ",""],"id":875},{"start":{"row":0,"column":0},"end":{"row":72,"column":12},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"]= 'mongodb+srv://ayaanh221:missayaan221@myfirstcluster-lj4yz.mongodb.net/diary-max?retryWrites=true&w=majority'","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","@app.route('/add_task')","def add_task():","    ","    return render_template('addtask.html',","                           categories=mongo.db.categories.find())","","                           ","@app.route('/task_recipe')","def recipes():","    return render_template(\"recipes.html\", tasks=mongo.db.tasks.find())","    ","","@app.route('/insert_task', methods=['POST'])","def insert_task():","   ","    tasks = mongo.db.tasks","    tasks.insert_one(request.form.to_dict())","    return redirect(url_for('get_tasks'))","    ","    ","    ","","","","@app.route('/edit_task/<task_id>')","def edit_task(task_id):","    the_task =  mongo.db.tasks.find_one({\"_id\": ObjectId(task_id)})","    all_categories =  mongo.db.categories.find()","    return render_template('edittask.html', task=the_task,","                           categories=all_categories)","","   ","   ","@app.route('/update_task/<get_tasks>', methods=[\"POST\"])","def update_task(task_id):","    tasks = mongo.db.tasks","    tasks.update( {'_id': ObjectId(task_id)},","    {","       'recipe_name':request.form.get('recipe_name'),","        'photo_link':request.form.get('photo_link'),","        'cooking_time': request.form.get('cooking_time'),","        'ingredients': request.form.get('ingredients'),","        'method': request.form.get('method'),","        'due_date': request.form.get('due_date'),","        'vegetarian':request.form.get('vegetarian')","    })","    return redirect(url_for('get_tasks'))","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)","            "]}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["t"],"id":876},{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":["a"]},{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["s"]}],[{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"insert","lines":["k"],"id":877},{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["_"]}],[{"start":{"row":26,"column":17},"end":{"row":26,"column":24},"action":"remove","lines":["_recipe"],"id":878},{"start":{"row":26,"column":13},"end":{"row":26,"column":20},"action":"insert","lines":["_recipe"]}],[{"start":{"row":26,"column":13},"end":{"row":26,"column":14},"action":"remove","lines":["_"],"id":879},{"start":{"row":26,"column":19},"end":{"row":26,"column":20},"action":"insert","lines":["_"]}],[{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"remove","lines":["s"],"id":880}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":8},"action":"remove","lines":["task"],"id":881},{"start":{"row":27,"column":11},"end":{"row":27,"column":15},"action":"insert","lines":["task"]}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"remove","lines":["_"],"id":882},{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"insert","lines":["_"]}],[{"start":{"row":26,"column":13},"end":{"row":26,"column":20},"action":"remove","lines":["recipe_"],"id":883},{"start":{"row":26,"column":17},"end":{"row":26,"column":24},"action":"insert","lines":["recipe_"]}],[{"start":{"row":26,"column":23},"end":{"row":26,"column":24},"action":"remove","lines":["_"],"id":884},{"start":{"row":26,"column":17},"end":{"row":26,"column":18},"action":"insert","lines":["_"]}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":11},"action":"remove","lines":["recipe_"],"id":885},{"start":{"row":27,"column":8},"end":{"row":27,"column":15},"action":"insert","lines":["recipe_"]}],[{"start":{"row":27,"column":14},"end":{"row":27,"column":15},"action":"remove","lines":["_"],"id":886},{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["_"]}],[{"start":{"row":26,"column":17},"end":{"row":26,"column":18},"action":"insert","lines":["s"],"id":887}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["s"],"id":888}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"remove","lines":["s"],"id":889}],[{"start":{"row":26,"column":17},"end":{"row":26,"column":18},"action":"remove","lines":["s"],"id":890}]]},"ace":{"folds":[],"customSyntax":"python","scrolltop":516.578125,"scrollleft":0,"selection":{"start":{"row":36,"column":31},"end":{"row":36,"column":32},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":33,"state":"start","mode":"ace/mode/python"}},"timestamp":1581109929968,"hash":"d7671052b4821e96309d5927e3ea3378bec33f3e"}