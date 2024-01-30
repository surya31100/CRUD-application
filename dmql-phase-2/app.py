from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import psycopg2.extras

app = Flask(__name__)

db_params = {
    'dbname': 'CSE560_Project_Football',
    'user': 'postgres',
    'password': 'pranav',
    'host': 'localhost',
    'port': '5433'   
}

def connect_to_db():
    conn = psycopg2.connect(**db_params)
    return conn

@app.route('/')
def index():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM leagues")
    leagues_data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', leagues=leagues_data)

@app.route('/players')
def players():
    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM players")
    players_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('positions.html', players = players_data)

@app.route('/positions', methods=['POST'])
def positions():
    player_id = request.form.get('id')

    conn = connect_to_db()
    cursor = conn.cursor()

    query = """
    SELECT p.name AS player_name, a.position, COUNT(*) AS appearances
    FROM appearences a
    JOIN players p ON a.playerID = p.playerID
    WHERE a.playerID = %s
    GROUP BY p.name, a.position
    ORDER BY appearances DESC;
    """

    cursor.execute(query, (player_id,))
    positions = cursor.fetchall()

    print(positions)
    
    cursor.close()
    conn.close()

    return render_template('positions.html', positions=positions)

@app.route('/top_goal_scorer')
def top_goal_scorer():
    return render_template("topGoals.html")

@app.route('/top_goals', methods=['POST'])
def top_goals():
    league_id = request.form.get('id')
    season = request.form.get('year')

    conn = connect_to_db()
    cursor = conn.cursor()

    query = """
    SELECT p.name AS player_name, l.name AS league_name, SUM(a.goals) AS total_goals
    FROM appearences a
    JOIN players p ON a.playerID = p.playerID
    JOIN games g ON a.gameID = g.gameID
    JOIN leagues l ON g.leagueID = l.leagueID
    WHERE l.leagueID = %s AND g.season = %s
    GROUP BY p.name, l.name
    ORDER BY total_goals DESC
    LIMIT 10;
    """
    cursor.execute(query, (league_id, season))
    results = cursor.fetchall()

    print(results)
    
    cursor.close()
    conn.close()

    return render_template('topGoals.html', results=results)

@app.route('/best_shooter_assister_combo')
def best_combo():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("""SELECT shooter.name AS shooter_name, assister.name AS assister_name, COUNT(*) AS combinations
                   FROM shots
                   JOIN players shooter ON shots.shooterID = shooter.playerID
                   JOIN players assister ON shots.assisterID = assister.playerID
                   GROUP BY shooter.name, assister.name
                   ORDER BY combinations DESC
                   LIMIT 10;""")
    
    combo_data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('bestShooterAssister.html', top_combinations=combo_data)


@app.route('/add_league', methods=['POST'])
def add_league():
    
    conn = connect_to_db()
    cursor = conn.cursor()

    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        unotation = request.form['unotation']
        
        cursor.execute("INSERT INTO leagues (leagueID, name, understatNotation) VALUES (%s,%s,%s)", (id, name, unotation))
        conn.commit()
        # flash('Student Added successfully')
        # return redirect(url_for('Index'))

        cursor.close()
        conn.close()

        # Redirect back to the index page
        return redirect(url_for('index'))
    
@app.route('/delete/<int:league_id>', methods=['GET'])
def delete_league(league_id):
    conn = connect_to_db()
    cursor = conn.cursor()

    # Delete the league by ID
    cursor.execute("DELETE FROM leagues WHERE leagueID = %s", (league_id,))
    conn.commit()

    cursor.close()
    conn.close()

    # Redirect back to the index page after deletion
    return redirect(url_for('index'))

@app.route('/edit/<int:league_id>', methods=['POST'])
def update_league(league_id):
    conn = connect_to_db()
    cursor = conn.cursor()

    # Get data from the edit form
    edit_name = request.form.get('edit_name')
    edit_understat_notation = request.form.get('edit_understatNotation')

    # Update the league details in the database
    cursor.execute("UPDATE leagues SET name = %s, understatNotation = %s WHERE leagueID = %s", (edit_name, edit_understat_notation, league_id))
    conn.commit()

    cursor.close()
    conn.close()

    # Redirect back to the index page after updating
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)


