import config
import telepot
from telepot.delegate import per_inline_from_id, create_open, pave_event_space


class InlineHandler(telepot.helper.InlineUserHandler, telepot.helper.AnswererMixin):
    def on_inline_query(self, msg):
        def compute_answer():
            query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
            if query_string == 'shrug':
                print('¯\_(ツ)_/¯')
                articles = [{'type': 'article',
                             'id': 'shrug',
                             'title': '¯\_(ツ)_/¯',
                             'message_text': '¯\_(ツ)_/¯ '}]
            elif query_string == 'tableflip':
                print('(╯°□°）╯︵ ┻━┻')
                articles = [{'type': 'article',
                             'id': 'tableflip',
                             'title': '(╯°□°）╯︵ ┻━┻',
                             'message_text': '(╯°□°）╯︵ ┻━┻'}]
            elif query_string == 'tableset':
                print('┬──┬ ノ( ゜-゜ノ)')
                articles = [{'type': 'article',
                             'id': 'tableset',
                             'title': '┬──┬ ノ( ゜-゜ノ)',
                             'message_text': '┬──┬ ノ( ゜-゜ノ)'}]
            elif query_string == 'disaproval':
                articles = [{'type': 'article',
                             'id': 'disaproval',
                             'title': 'ಠ_ಠ',
                             'message_text': 'ಠ_ಠ'}]
            elif query_string == 'lenny':
                articles = [{'type': 'article',
                             'id': 'lenny',
                             'title': '( ͡° ͜ʖ ͡°)',
                             'message_text': '( ͡° ͜ʖ ͡°)'}]
            else:
                articles = [{'type': 'article',
                             'id': 'error',
                             'title': 'Text smiley is not found',
                             'message_text': 'Text smiley is not found'}]

            print(self.id, ':', 'Inline Query:', query_id, from_id, query_string)

            return articles

        self.answerer.answer(msg, compute_answer)

    def on_chosen_inline_result(self, msg):
        from pprint import pprint
        pprint(msg)
        result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
        print(self.id, ':', 'Chosen Inline Result:', result_id, from_id, query_string)


bot = telepot.DelegatorBot(config.token, [
    pave_event_space()(
        per_inline_from_id(), create_open, InlineHandler, timeout=100000),
])
bot.message_loop(run_forever='Listening ...')
