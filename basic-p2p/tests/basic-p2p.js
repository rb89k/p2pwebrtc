'use strict';

module.exports = {
  'Basic P2P Test' : function (browser) {
    const env_key = process.env.__NIGHTWATCH_ENV_KEY;
    // console.log("ENV_KEY", env_key);
    const passiveClient = env_key.endsWith('_1');
    browser.url(`${browser.launchUrl}/basic-p2p/#4134710`);

    if (passiveClient) {
      browser.click('#call-button');
      browser.pause(500);
      browser.assert.domPropertyEquals('#peer', 'readyState', 4);
      browser.pause(1000);
    } else {
      browser.expect.element('#header h1').text.to.equal('Welcome to Room #4134710');
      browser.assert.visible('#self');
      browser.assert.visible('#peer');
      browser.assert.domPropertyEquals('#self', 'readyState', 4);
      browser.click('#call-button');
      browser.pause(500);
      browser.assert.domPropertyEquals('#peer', 'readyState', 4);
      browser.pause(1000);
    }

    browser.end();

  }
};
