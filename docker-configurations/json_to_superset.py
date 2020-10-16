import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from uuid import uuid4
from datetime import datetime

postgres_username="superset"
postgres_password="superset"
postgres_host="127.0.0.1"
postgres_database="superset"

DB_URL = 'postgresql+psycopg2://{}:{}@{}/{}'.\
        format(postgres_username, \
        postgres_password, \
        postgres_host,
        postgres_database)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Docker_Bench(db.Model):
    __tablename__ = 'docker_bench'
    uid = db.Column(db.String(50), primary_key=True)
    test_id = db.Column(db.String(10), nullable=False)
    test_description = db.Column(db.String(100), nullable=False)
    result_id = db.Column(db.String(10), nullable=False)
    result_description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False)

def main():

    db.drop_all()
    db.create_all()

    with open("docker-bench-security.sh.log.json") as fr:

        content = json.loads(fr.read())
    
    for test in content["tests"]:

        test_id = test["id"]
        test_description = test["desc"]

        for result in test["results"]:
            # uid = str(uuid4())
            uid = datetime.now().isoformat()
            result_id = result["id"]
            result_description = result["desc"]
            status = result["result"]

            docker_bench_item = Docker_Bench(uid=uid,test_id=test_id,\
                test_description=test_description,result_id=result_id, \
                result_description=result_description,status=status)
            db.session.add(docker_bench_item)
            db.session.commit()

    print("Done!")

if __name__ == "__main__":
    main()