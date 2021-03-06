cd $PROOTPATH/quic-implementations/aioquic
curl https://sh.rustup.rs -sSf | sh -s -- -y
git stash
git checkout 0.9.3 
export PYTHONPATH=$PWD
source $HOME/.cargo/env

python3 -m pip uninstall --yes setuptools
python3 -m pip uninstall --yes cryptography
python3 -m pip uninstall --yes cffi
python3 -m pip uninstall --yes setuptools_rust
python3 -m pip install --upgrade launchpadlib
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade cryptography
python3 -m pip install --upgrade cffi
python3 -m pip install setuptools_rust
python3 -m pip install -e .
python3 -m pip install aiofiles asgiref dnslib httpbin starlette wsproto

rm $PROOTPATH/quic-implementations/aioquic/examples/http3_client.py
cp $PROOTPATH/ressources/aioquic/http3_client.py $PROOTPATH/quic-implementations/aioquic/examples/http3_client.py
