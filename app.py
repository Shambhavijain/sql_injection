from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Helper function to get database connection
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row # This allows us to access columns by name
    return conn

@app.route("/")
def index():
    return redirect(url_for("vote"))

@app.route("/vote", methods=["GET","POST"])
def vote():
    message = None
    if request.method == "POST":
        u = request.form["user_id"]
        c = request.form["candidate_id"]

        conn = get_db_connection()
        cur = conn.cursor()

        #  Vulnerable: direct string formatting - NOW A SINGLE LINE
        query = f"INSERT INTO votes(user_id, candidate_id, vote_count) VALUES ('{u}', '{c}', 1);" 

        try:
           
            # This line makes stacked queries possible for demonstration
            cur.executescript(query)
            #  END TEMPORARY CHANGE 

            conn.commit()
            message = f"Vote for candidate {c} recorded successfully for user {u}!"
        except sqlite3.Error as e:
            message = f"Error casting vote: {e}"
            conn.rollback()
        finally:
            conn.close()

    return render_template("vote.html", message=message)



@app.route("/results")
def results():
    s = request.args.get("search", "")

    conn = get_db_connection()
    cur = conn.cursor()

    
    # This new query will normally return nothing unless the injected 's' makes it true.

    q = f"SELECT user_id, candidate_id, vote_count FROM votes WHERE user_id = 'NON_EXISTENT_ID_FOR_FILTER' AND user_id = '{s}'"
    
    results = []
    try:
        cur.execute(q)
        results = cur.fetchall()
    except sqlite3.Error as e:
        print(f"Database error during search: {e}")
        results = []
    finally:
        conn.close()

    return render_template("results.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)