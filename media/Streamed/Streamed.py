from flask import Flask, flash, redirect, render_template, request, session, Response, jsonify
from helpers import login_required

#bro how tf am i supposed to understand this and write actual documentation in 3 months
def register_routes(app):

    @app.route("/videos")
    @login_required
    def videos():
        if request.method == "GET":
            #tags = db.execute('FROM vTags SELECT *')
            #print(tags)

            # TODO: choose 5 random categories

            return(render_template("videos.html"))