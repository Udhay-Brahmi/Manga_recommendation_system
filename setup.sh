mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORTS\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml