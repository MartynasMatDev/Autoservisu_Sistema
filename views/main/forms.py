from django import forms

# Carbon Design System form control classes, keyed by Django widget type.
CARBON_CLASSES = {
    forms.CheckboxInput: "cds--checkbox",
    forms.CheckboxSelectMultiple: "cds--checkbox",
    forms.RadioSelect: "cds--radio-button",
    forms.Select: "cds--select-input",
    forms.Textarea: "cds--text-area",
}
INPUT_CLASS = "cds--text-input"
# Django 6.1's default blank choice is the English "- Select an option -".
BLANK_CHOICE_LABEL = "- Pasirinkite -"
INVALID_CLASSES = {
    "cds--text-input": "cds--text-input--invalid",
    "cds--text-area": "cds--text-area--invalid",
}


class CarbonFormMixin(forms.BaseForm):
    """Give every widget its Carbon class (markup lives in partials/form_fields)."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            css = next(
                (c for w, c in CARBON_CLASSES.items() if isinstance(widget, w)),
                INPUT_CLASS,
            )
            widget.attrs["class"] = css
            if isinstance(field, forms.ModelChoiceField):
                if field.empty_label is not None:
                    field.empty_label = BLANK_CHOICE_LABEL
            elif isinstance(field, forms.ChoiceField):
                choices = list(field.choices)
                if choices and choices[0][0] == "":
                    choices[0] = ("", BLANK_CHOICE_LABEL)
                    field.choices = choices

    def full_clean(self):
        super().full_clean()
        for name in self.errors:
            if name in self.fields:
                attrs = self.fields[name].widget.attrs
                invalid = INVALID_CLASSES.get(attrs.get("class", ""))
                if invalid:
                    attrs["class"] += f" {invalid}"
                attrs["aria-invalid"] = "true"


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.TimeInput):
    input_type = "time"
