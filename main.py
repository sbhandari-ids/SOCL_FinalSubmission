#!/Users/SB/Documents/CT_WorkSpace/SOCL_FinalSubmission/venv/bin/python3

from website import create_app

app  = create_app()

if __name__ == '__main__':
    app.run(debug=True) 