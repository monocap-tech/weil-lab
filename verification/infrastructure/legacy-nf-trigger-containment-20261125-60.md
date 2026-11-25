# Final two observed NF PR fan-out gates

NF501 and NF504 had existing branch- and path-scoped push triggers but unrestricted pull_request triggers. Copied their exact existing push path lists to pull_request, preserving both push and manual dispatch, and all job bodies. Detached, not activated.
