from typing import Any
from falcon import Request
from ioclib.injector import Requirement, void


def header(default=void) -> Any:
    return Requirement[Any](None, None, 'falcon/header', default)


def parameter(default=void) -> Any:
    return Requirement[Any](None, None, 'falcon/parameter', default)


def context(default=void) -> Any:
    return Requirement[Any](None, Any, 'falcon/context', default)


def falcon_request_injector(requirement: Requirement[Any], args: tuple[Any, ...], kwargs: dict[str, Any]) -> Any:
    if not requirement.location.startswith('falcon'):
        raise LookupError()

    assert requirement.name

    request = next((arg for arg in args if isinstance(arg, Request)), None)

    if not request:
        raise ValueError()

    if requirement.location == 'falcon/parameter':
        if str in requirement.types:
            return request.get_param(requirement.name, False)

        if int in requirement.types:
            return request.get_param_as_int(requirement.name, False)

        if float in requirement.types:
            return request.get_param_as_float(requirement.name, False)

        if list in requirement.types:
            return request.get_param_as_list(requirement.name, False)

        if dict in requirement.types:
            return request.get_param_as_json(requirement.name, False)

        raise ValueError()

    if requirement.location == 'falcon/context':
        return getattr(request.context, requirement.name)

    if requirement.location == 'falcon/header':
        raise NotImplementedError()
