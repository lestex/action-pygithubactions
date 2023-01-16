from pygithubactions import core
from pygithubactions.core.utils import AnnotationProperties


def main():
    # get input
    test_input = core.get_input('test_input', required=True)
    test_bool_input = core.get_input('test_bool_input')
    test_multiline_input = core.get_multiline_input('test_multiline_input')

    output_value = {
        'test_input': test_input,
        'test_bool_input': test_bool_input,
        'test_multiline_input': test_multiline_input,
    }

    # print out inputs
    core.info(f'Test input: {test_input}')
    core.info(f'Test input: {test_bool_input}')
    core.info(f'Test boolean_input: {test_multiline_input}')
    core.set_output('output', output_value)

    # set env variable
    core.export_variable('envvar1', 'value')

    # mask secret
    core.set_secret('mypassword')

    # Wrap a function call
    def do_some_job():
        core.info('This inside a do_some_job() function')
        return 'result'

    # Manually wrap output
    core.start_group('Do some function')
    do_some_job()
    core.end_group()

    # Auto wrap
    result = core.group('Do something wrapped', do_some_job)
    core.info(f'This is a result: {result}')
    
    # test annotations
    annotation_properties1 = AnnotationProperties()
    core.error('Test `error` message', annotation_properties1)
    core.warning('Test `warning` message', annotation_properties1)
    core.notice('Test `notice` message', annotation_properties1)


if __name__ == '__main__':
    main()
