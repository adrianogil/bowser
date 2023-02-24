if [ -z "$BOWSER_PYTHON_PATH" ]
then
    export BOWSER_PYTHON_PATH=$BOWSER_DIRS/python/
    export PYTHONPATH=$BOWSER_PYTHON_PATH:$PYTHONPATH
fi

alias bowser="python3 -m bowser"
alias bw="python3 -m bowser"

