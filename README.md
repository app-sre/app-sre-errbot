# WIP: ChatOps bot for App-SRE
Build using [Errbot](https://github.com/errbotio/errbot/)

# Running

The bot expects the SLACK_TOKEN environment variable to be defined in order to connect to slack

The app-interface plugin expects the GQL_SERVER and GQL_TOKEN environment variables to be defined to connect to graphql

    export SLACK_TOKEN="xoxb-..."
    export GQL_SERVER="https://graphql.example.com/graphql"
    export GQL_TOKEN="..."
    make run

