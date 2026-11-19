// Verificarea automată a extensiei JW Safari (6.1.6, pasul 3 din audit).
// Prinde ce a produs regresiile din 6.1.0 și 6.1.4: variabile nedefinite, globale folosite din greșeală
// (de exemplu „close” = window.close), cod de neatins și declarații duplicate.
import globals from 'globals';
export default [{
  files: ['**/*.js'],
  languageOptions: {
    ecmaVersion: 2022, sourceType: 'script',
    globals: { ...globals.browser, GM: 'readonly', GM_getValue: 'readonly', GM_setValue: 'readonly', GM_xmlhttpRequest: 'readonly', GM_info: 'readonly', unsafeWindow: 'readonly', define: 'readonly', module: 'writable', exports: 'writable' }
  },
  rules: {
    'no-undef': 'error',
    'no-restricted-globals': ['error', 'close', 'name', 'length', 'event', 'status', 'top', 'parent', 'self', 'origin', 'stop', 'open', 'find', 'print', 'blur', 'focus', 'scroll'],
    'no-unreachable': 'error',
    'no-dupe-keys': 'error',
    'no-redeclare': 'error',
    'no-unused-vars': ['warn', { vars: 'local', args: 'none', caughtErrors: 'none' }],
    'no-self-assign': 'error',
    'no-dupe-else-if': 'error',
    'no-unsafe-finally': 'error'
  }
}];
