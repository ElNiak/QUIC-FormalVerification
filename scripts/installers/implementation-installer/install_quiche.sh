 
cd $PROOTPATH/quic-implementations/
# install RUST
curl https://sh.rustup.rs -sSf | sh -s -- -y
source $HOME/.cargo/env
cd quiche/
cargo build --examples
cargo test
