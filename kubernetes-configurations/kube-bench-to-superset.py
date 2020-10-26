from sqlalchemy import create_engine, Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from uuid import uuid4
from datetime import datetime
import json; import os

postgres_username=os.environ['POSTGRES_USERNAME']
postgres_password=os.environ['POSTGRES_PASSWORD']
postgres_host=os.environ['POSTGRES_HOST']
postgres_database=os.environ['POSTGRES_DATABASE']

folder = "./kube-bench-examples/"

db_string = 'postgresql+psycopg2://{}:{}@{}/{}'.\
        format(postgres_username, 
        postgres_password, 
        postgres_host,
        postgres_database)

db = create_engine(db_string)  
base = declarative_base()

class Kube_Bench(base):
    __tablename__ = 'kube_bench'
    uid = Column(String(50), primary_key=True)
    time = Column(String(50), nullable=False)
    node_type = Column(String(50), nullable=False)
    section_id = Column(String(50), nullable=False)
    section_description = Column(String(255), nullable=False)
    test_id = Column(String(50), nullable=False)
    test_description = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False)

kubernetes_result_list = []

def load_kube_bench_results_in_list(file_name):

    with open(os.path.join(folder, file_name)) as fr:
        kube_bench_data = json.loads(fr.read())

    # Kube-Bench Master
    if kube_bench_data:
        node_type = kube_bench_data["node_type"].capitalize()
        
        for test in kube_bench_data["tests"]:
            
            section_id = test["section"]
            section_description = test["desc"]

            for result in test["results"]:
                uid = str(uuid4())
                test_id = result["test_number"]
                test_description = result["test_desc"]
                status = result["status"]
                
                # Adding to the list
                kubernetes_result_list.append({
                    "uid": uid,
                    "time": datetime.now().isoformat(),
                    "node_type": node_type,
                    "section_id": section_id,
                    "section_description": section_description,
                    "test_id": test_id,
                    "test_description": test_description,
                    "status": status
                })

def main():

    Session = sessionmaker(db)  
    session = Session()

    base.metadata.drop_all(db)
    base.metadata.create_all(db)

    kube_bench_files = ['kube-bench_master_output.json',
        'kube-bench_node_output.json']

    for kb_file in kube_bench_files:
        load_kube_bench_results_in_list(kb_file)

    for kubernetes_result_item in kubernetes_result_list:
    
        kube_bench_item = Kube_Bench(uid=kubernetes_result_item["uid"],
                time=kubernetes_result_item["time"],
                node_type=kubernetes_result_item["node_type"],
                section_id=kubernetes_result_item["section_id"],
                section_description=kubernetes_result_item["section_description"],
                test_id=kubernetes_result_item["test_id"],
                test_description=kubernetes_result_item["test_description"],
                status=kubernetes_result_item["status"])
    
        session.add(kube_bench_item)
        session.commit()
    session.close()
      
if __name__ == "__main__":
    main()