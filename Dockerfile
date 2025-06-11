FROM ghcr.io/astral-sh/uv:python3.12-alpine

RUN apk add --update nodejs npm
RUN npm install -g npm@latest
RUN npm install -g @modelcontextprotocol/inspector

RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app
RUN uv pip install -r requirements.txt --system

# COPY . /app
# ENTRYPOINT [ "fastmcp", "dev", "server.py:mcp" ]