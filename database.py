from sqlalchemy import create_engine, text
import os

string_connection = os.environ['db_connection_string']

engine = create_engine(string_connection,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

def load_jobs_position_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs_position = []
    for job in result.all():
      jobs_position.append(job._asdict())
    return jobs_position  

def load_job_position(id):
    with engine.connect() as conn:
      result = conn.execute(text(
        f"SELECT * FROM jobs WHERE id = :val"
      ),
         {"val": id}                   
      )
      job_position = result.mappings().all()
      if len(job_position) == 0:
        return None
      else:
        return dict(job_position[0])