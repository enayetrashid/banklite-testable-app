async function apiRequest(url, method, body) {
    const options = {
        method: method,
        headers: {
            "Content-Type": "application/json",
        },
    };

    if (body !== undefined) {
        options.body = JSON.stringify(body);
    }

    const response = await fetch(url, options);
    const data = await response.json();

    if (!response.ok) {
        const message = data.message || "Request failed.";
        throw new Error(message);
    }

    return data;
}

window.bankliteApi = {
    login(username, password) {
        return apiRequest("/api/login", "POST", {
            username: username,
            password: password,
        });
    },

    getBalance(accountId) {
        return apiRequest(`/api/accounts/${accountId}/balance`, "GET");
    },

    deposit(accountId, amount) {
        return apiRequest(`/api/accounts/${accountId}/deposit`, "POST", {
            amount: amount,
        });
    },

    withdraw(accountId, amount) {
        return apiRequest(`/api/accounts/${accountId}/withdraw`, "POST", {
            amount: amount,
        });
    },

    transfer(accountId, targetAccountId, amount) {
        return apiRequest(`/api/accounts/${accountId}/transfer`, "POST", {
            target_account_id: targetAccountId,
            amount: amount,
        });
    },

    getTransactions(accountId) {
        return apiRequest(`/api/accounts/${accountId}/transactions`, "GET");
    },
};
