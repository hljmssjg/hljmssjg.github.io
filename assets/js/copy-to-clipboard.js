document.addEventListener('DOMContentLoaded', function () {
    var codeBlocks = document.querySelectorAll('pre > code');

    codeBlocks.forEach(function(codeBlock) {
        var button = document.createElement('button');
        button.textContent = 'Copy';
        button.classList.add('copy-button');
        codeBlock.parentNode.insertBefore(button, codeBlock.nextSibling);

        var clipboard = new ClipboardJS(button, {
            target: function(trigger) {
                return trigger.previousSibling;  // 只复制 <code> 内容
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
