# import sdk.geetest
from sdk.geetest import GeetestLib
captach_id = "ae4c772ec8b41372b7a6e7d6895af9fa"
private_key = "2fac1f95451534364435934ea61adc08"
from sdk.geetest import *


class PcGetCaptchaHandler(SessionBaseHandler):
    def get(self):
        user_id = 'test'
        gt = GeetestLib(captach_id, private_key)
        status = gt.pre_process(user_id)
        if not status:
            status=2
        self.session[gt.GT_STATUS_SESSION_KEY] = status
        self.session["user_id"] = user_id
        response_str = gt.get_response_str()
        self.write(response_str)


class PcAjaxValidateHandler(SessionBaseHandler):
    def post(self):
        gt = GeetestLib(private_key, private_key)
        challenge = self.get_argument(gt.FN_CHALLENGE, "")
        validate = self.get_argument(gt.FN_VALIDATE, "")
        seccode = self.get_argument(gt.FN_SECCODE, "")
        status = self.session[gt.GT_STATUS_SESSION_KEY]

        user_id = self.session["user_id"]
        if status == 1:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        self.session["user_id"] = user_id

        result = {"status": "success"} if result else {"status": "fail"}
        self.write(json.dumps(result))