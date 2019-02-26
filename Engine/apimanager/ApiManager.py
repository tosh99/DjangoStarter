from Engine.utilities.utilities import ResponseHelper, Logger
import json
from Engine.utilities import constants as cnts


class APIManager:

    def resolve_context(self, request):
        try:


            ''' Step 1 >> Validate Input JSON ---------------------------------'''
            try:
                inputs = json.loads(request.body)
            except Exception as e:
                return ResponseHelper().response(cnts.ERR_INVALID_REQUEST_TYPE['payload'], cnts.ERR_INVALID_REQUEST_TYPE['code'], cnts.ERR_INVALID_REQUEST_TYPE['message'])



            ''' Step 2 >> Resolve Context -------------------------------------'''
            try:
                context = inputs['context']
            except Exception as e:
                Logger().log_error(e)
                return ResponseHelper().response(cnts.ERR_INVALID_CONTEXT['payload'], cnts.ERR_INVALID_CONTEXT['code'], cnts.ERR_INVALID_CONTEXT['message'])



            ''' Step 3 >> Fire Business Rule  ---------------------------------'''
            try:
                pass
            except Exception as e:
                Logger().log_error(e)
                return ResponseHelper().response(cnts.ERR_PROCESS_FAILED['payload'], cnts.ERR_PROCESS_FAILED['code'], cnts.ERR_PROCESS_FAILED['message'])



            ''' Step 4 >> Return Response  -------------------------------------'''
            return ResponseHelper().response()


        except Exception as e:
            Logger().log_error(e)
            return ResponseHelper().response(cnts.ERR_PROCESS_FAILED['payload'], cnts.ERR_PROCESS_FAILED['code'], cnts.ERR_PROCESS_FAILED['message'])
