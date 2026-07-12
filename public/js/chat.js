// ======================== 聊天模块 ========================

async function loadChatMessages(orderId) {
  return apiGet("/api/chat/" + orderId);
}

async function sendChatMessage(orderId, sender, message, image) {
  if (image) {
    var fd = new FormData();
    fd.append("sender", sender);
    fd.append("message", message || "");
    fd.append("image", image);
    var r = await fetch("/api/chat/" + orderId, { method: "POST", body: fd });
    if (!r.ok) throw new Error("发送失败");
    return r.json();
  }
  return apiPost("/api/chat/" + orderId, { sender: sender, message: message || "" });
}