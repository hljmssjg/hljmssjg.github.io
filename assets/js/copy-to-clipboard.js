document.addEventListener('DOMContentLoaded', function() {
    // 为所有代码块添加 Copy 按钮
    document.querySelectorAll('pre > code').forEach(function(codeBlock) {
        const pre = codeBlock.parentNode;
        const button = document.createElement('button');
        button.className = 'copy-button';
        button.textContent = 'Copy';
        pre.appendChild(button); // 插入到 <pre> 内部

        // 初始化 ClipboardJS
        const clipboard = new ClipboardJS(button, {
            target: () => codeBlock // 复制 <code> 内容
        });

        // 复制成功提示
        clipboard.on('success', function(e) {
            e.clearSelection();
            const notification = document.createElement('div');
            notification.className = 'copy-notification';
            notification.textContent = 'Copied!';
            document.body.appendChild(notification);
            setTimeout(() => notification.remove(), 2000);
        });

        // 复制失败提示（可选）
        clipboard.on('error', function(e) {
            console.error('复制失败:', e.action);
        });
    });
});