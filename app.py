from flask import Flask,jsonify,request
import ipl
import juggad
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World"

@app.route("/api/teams")
def teams():
    teams = ipl.team()
    return jsonify(teams)

@app.route("/api/teamvteam")
def teamvteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = ipl.teamVTeamAPI(team1,team2)

    if response:
        return jsonify(response)

@app.route("/api/team")
def team():
    team = request.args.get('team')

    response = juggad.teamAPI(team)
    if response:
        return response

@app.route("/api/batsman_record")
def batsman_record():
    batsman = request.args.get('batsman')

    response = juggad.batsmanRecord(batsman)
    if response:
        return response



@app.route("/api/bowler_record")
def bowler_record():
    bowler = request.args.get('bowler')

    response = juggad.bowlerRecord(bowler)
    return response


app.run(debug=True)