from nicegui import ui

ui.label('📋 ')
ui.input('你的名字')
ui.button('提交', on_click=lambda: ui.notify('感谢提交！'))

ui.run()
