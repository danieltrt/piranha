argument_mappings = {
    "api_type": "api_type",
    "api_key": "api_key",
    "api_base": "azure_endpoint",
    "api_version": "api_version",
}

args = []
for arg, new_constructor in argument_mappings.items():
    match f"cs openai_api.{arg} = :[x]"
    replace with ""
    args += f"{new_constructor} = :[x]"

append("AzureOpenAI(args)")