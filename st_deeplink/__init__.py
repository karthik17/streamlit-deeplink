import inspect
import streamlit as st


def convert_query_params_to_dict(query_params):
    query_params = ({} if query_params == '' else query_params)
    return query_params


def deep_link(widget_f, key=None):
    """Return a function that wraps a streamlit widget.
    It also
    1) Saves widget's values to query parameters.
    2) Uses existing query parameters to set default value.
    """
    def wrapper(*args, **kwargs):
        query_params = convert_query_params_to_dict(st.experimental_get_query_params())
        bound_args = inspect.signature(widget_f).bind(*args, **kwargs)
        param_name = (bound_args.arguments['key'] if 'key' in bound_args.arguments else key)
        if param_name is None:
            raise Exception("Please pass the parameter 'key' for the streamlit widget.")
        if widget_f.__name__ == 'selectbox':
            if (('is_first_time' in st.session_state) and (st.session_state['is_first_time']) and
                    (param_name in query_params)):
                st.session_state[param_name] = query_params[param_name][0]
            param_value = widget_f(**bound_args.arguments)
            query_params[param_name] = param_value
        elif widget_f.__name__ == 'multiselect':
            if (('is_first_time' in st.session_state) and (st.session_state['is_first_time']) and
                    (param_name in query_params)):
                st.session_state[param_name] = query_params[param_name]
            param_value = widget_f(**bound_args.arguments)
            query_params[param_name] = param_value
        else:
            param_value = widget_f(*args, **kwargs)

        st.experimental_set_query_params(**query_params)
        return param_value
    return wrapper


def update_query_params(qp_dict):
    query_params = convert_query_params_to_dict(st.experimental_get_query_params())
    query_params.update(qp_dict)
    st.experimental_set_query_params(**query_params)
    return
