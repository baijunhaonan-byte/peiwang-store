// ======================== Auth Header ========================
function getAuthHeaders() {
  var t = localStorage.getItem('peiwang_token');
  if (t) return { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + t };
  return { 'Content-Type': 'application/json' };
}

function getAuthHeadersGet() {
  var t = localStorage.getItem('peiwang_token');
  if (t) return { 'Authorization': 'Bearer ' + t };
  return {};
}

// ======================== API 工具 ========================

async function apiGet(url) {
  const r = await fetch(url, { headers: getAuthHeadersGet() });
  if (!r.ok) throw new Error("请求失败");
  return r.json();
}

async function apiPost(url, data) {
  const r = await fetch(url, {
    method: "POST",
    headers: getAuthHeaders(),
    body: JSON.stringify(data)
  });
  if (!r.ok) throw new Error("请求失败");
  return r.json();
}

async function apiPut(url, data) {
  const r = await fetch(url, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  if (!r.ok) throw new Error("请求失败");
  return r.json();
}

async function apiDelete(url) {
  const r = await fetch(url, { method: "DELETE" });
  if (!r.ok) throw new Error("请求失败");
  return r.json();
}

// ======================== SSE 实时连接 ========================
const sseCallbacks = {};

function connectSSE() {
  const evtSource = new EventSource("/api/events");
  evtSource.addEventListener("new_order", (e) => {
    const data = JSON.parse(e.data);
    if (sseCallbacks.onNewOrder) sseCallbacks.onNewOrder(data);
  });
  evtSource.addEventListener("order_update", (e) => {
    const data = JSON.parse(e.data);
    if (sseCallbacks.onOrderUpdate) sseCallbacks.onOrderUpdate(data);
  });
  evtSource.addEventListener("chat_message", (e) => {
    const data = JSON.parse(e.data);
    if (sseCallbacks.onMessage) sseCallbacks.onMessage(data);
  });
  evtSource.addEventListener("menu_update", (e) => {
    const data = JSON.parse(e.data);
    if (sseCallbacks.onMenuUpdate) sseCallbacks.onMenuUpdate(data);
  });
  evtSource.onerror = () => {
    console.warn("SSE 连接断开，5秒后重连...");
    setTimeout(connectSSE, 5000);
  };
}