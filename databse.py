from sqlalchemy import create_engine, text

string_connection = "mysql+pymysql://cfgwuw43a7yvbao4jxzp:pscale_pw_U7ktU9cmQlT2ZcB6hZY6GRDYky31EBnwtg0JpPD65Vf@aws.connect.psdb.cloud/flaskjobs?charset=utf8mb4"

engine = create_engine(string_connection,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM jobs"))
  result_dict = []
  for job in result.all():
    result_dict.append(job._asdict())
    print(result_dict)
