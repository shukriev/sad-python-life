class DictHelper(object):

    @staticmethod
    def recursive_search(dictionary: dict, keyword: str):
        for k, v in dictionary.items():
            if isinstance(v, dict):
                return DictHelper.recursive_search(v, keyword)

            if k == keyword:
                return v
