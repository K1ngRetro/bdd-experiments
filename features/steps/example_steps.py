from behave import given, when, then
import json
import allure


def _attach_text(name, text):
    allure.attach(text, name=name, attachment_type=allure.attachment_type.TEXT)


def _attach_json(name, obj):
    allure.attach(
        json.dumps(obj, indent=2, sort_keys=True),
        name=name,
        attachment_type=allure.attachment_type.JSON,
    )

@given('I have numbers {num1:d} and {num2:d}')
def step_given_numbers(context, num1, num2):
    context.num1 = num1
    context.num2 = num2
    _attach_json("numbers", {"num1": num1, "num2": num2})

@when('I add them')
def step_when_add(context):
    context.result = context.num1 + context.num2
    _attach_json("operation", {"op": "add", "result": context.result})

@when('I subtract them')
def step_when_subtract(context):
    context.result = context.num1 - context.num2
    _attach_json("operation", {"op": "subtract", "result": context.result})

@when('I multiply them')
def step_when_multiply(context):
    context.result = context.num1 * context.num2
    _attach_json("operation", {"op": "multiply", "result": context.result})

@then('the result should be {expected:d}')
def step_then_result(context, expected):
    _attach_json("assert", {"expected": expected, "actual": context.result})
    assert context.result == expected

@given('I have JSON object A:')
def step_given_json_a(context):
    context.json_a = json.loads(context.text)
    _attach_text("json_a_raw", context.text)
    _attach_json("json_a_parsed", context.json_a)

@given('I have JSON object B:')
def step_given_json_b(context):
    context.json_b = json.loads(context.text)
    _attach_text("json_b_raw", context.text)
    _attach_json("json_b_parsed", context.json_b)

@then('the JSON objects should be equal')
def step_then_json_equal(context):
    diffs = []
    _collect_json_diffs(context.json_a, context.json_b, path="$", diffs=diffs)
    _attach_json("json_compare", {"diffs": diffs})
    if diffs:
        raise AssertionError("JSON mismatch:\n" + "\n".join(diffs))


def _collect_json_diffs(a, b, path, diffs):
    if type(a) is not type(b):
        diffs.append(f"{path}: type {type(a).__name__} != {type(b).__name__}")
        return

    if isinstance(a, dict):
        a_keys = set(a.keys())
        b_keys = set(b.keys())
        for key in sorted(a_keys - b_keys):
            diffs.append(f"{path}.{key}: missing in B")
        for key in sorted(b_keys - a_keys):
            diffs.append(f"{path}.{key}: missing in A")
        for key in sorted(a_keys & b_keys):
            _collect_json_diffs(a[key], b[key], f"{path}.{key}", diffs)
        return

    if isinstance(a, list):
        if len(a) != len(b):
            diffs.append(f"{path}: length {len(a)} != {len(b)}")
        for i in range(min(len(a), len(b))):
            _collect_json_diffs(a[i], b[i], f"{path}[{i}]", diffs)
        return

    if a != b:
        diffs.append(f"{path}: {a!r} != {b!r}")
