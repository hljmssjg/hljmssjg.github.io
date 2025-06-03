document.addEventListener('DOMContentLoaded', function () {
    // 只选择在 <pre> 里的 <code> 标签，排除行内代码
    var codeBlocks = document.querySelectorAll('pre > code');

    codeBlocks.forEach(function(codeBlock) {
        var button = document.createElement('button');
        button.textContent = 'Copy';
        button.classList.add('copy-button'); // 添加按钮样式类
        codeBlock.parentNode.insertBefore(button, codeBlock.nextSibling);

        var clipboard = new ClipboardJS(button, {
            target: function (trigger) {
                // 复制父元素 <pre> 的文本内容
                return trigger.previousSibling.parentNode;
            }
        });

        clipboard.on('success', function (e) {
            e.clearSelection();
            var notification = document.createElement('div');
            notification.textContent = 'Copied!';
            notification.classList.add('notification');
            document.body.appendChild(notification);
            setTimeout(function () {
                notification.style.opacity = '0';
                setTimeout(function () {
                    document.body.removeChild(notification);
                }, 1000);
            }, 1000);
        });

        clipboard.on('error', function (e) {
            console.error('复制失败:', e.action);
        });
    });
});
