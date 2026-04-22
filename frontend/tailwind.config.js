import frappeUIPreset from 'frappe-ui/tailwind'

export default {
	presets: [frappeUIPreset],
	content: [
		'./index.html',
		'./src/**/*.{vue,js,ts,jsx,tsx}',
		'./node_modules/frappe-ui/src/**/*.{vue,js,ts,jsx,tsx}',
		'../node_modules/frappe-ui/src/**/*.{vue,js,ts,jsx,tsx}',
		'./node_modules/frappe-ui/frappe/**/*.{vue,js,ts,jsx,tsx}',
		'../node_modules/frappe-ui/frappe/**/*.{vue,js,ts,jsx,tsx}',
	],
	theme: {
		extend: {
			colors: {
				primary: {
					50: '#FBF7ED',
					100: '#F5ECD1',
					200: '#ECD7A3',
					300: '#DFBC6E',
					400: '#D4AF7A',
					500: '#C9A961',
					600: '#B08F4A',
					700: '#8C6F36',
					800: '#634F27',
					900: '#3F321A',
				},
			},
			strokeWidth: {
				1.5: '1.5',
			},
			screens: {
				'2xl': '1600px',
				'3xl': '1920px',
			},
		},
	},
	plugins: [],
}
